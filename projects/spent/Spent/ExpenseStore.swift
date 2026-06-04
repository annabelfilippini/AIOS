import Foundation
import WidgetKit

@MainActor
final class ExpenseStore: ObservableObject {
    @Published private(set) var expenses: [Expense] = [] {
        didSet {
            ExpenseStorage.save(expenses)
        }
    }

    private let calendar = Calendar.current

    init() {
        load()
    }

    var todayTotal: Decimal {
        expenses
            .filter { calendar.isDateInToday($0.createdAt) }
            .reduce(Decimal.zero) { $0 + $1.amount }
    }

    var monthTotal: Decimal {
        expenses
            .filter { calendar.isDate($0.createdAt, equalTo: Date(), toGranularity: .month) }
            .reduce(Decimal.zero) { $0 + $1.amount }
    }

    var recentExpenses: [Expense] {
        expenses.sorted { $0.createdAt > $1.createdAt }
    }

    var weeklySummaries: [SpendingSummary] {
        summaries(component: .weekOfYear, limit: 4)
    }

    var monthlySummaries: [SpendingSummary] {
        summaries(component: .month, limit: 4)
    }

    func add(amount: Decimal, item: String) {
        let cleanedItem = item.trimmingCharacters(in: .whitespacesAndNewlines)
        guard amount > 0, !cleanedItem.isEmpty else {
            return
        }

        expenses.append(Expense(amount: amount, item: cleanedItem))
    }

    func delete(_ expense: Expense) {
        expenses.removeAll { $0.id == expense.id }
    }

    func reloadFromStorage() {
        let storedExpenses = ExpenseStorage.load()
        if storedExpenses != expenses {
            expenses = storedExpenses
        }
    }

    private func load() {
        expenses = ExpenseStorage.load()
    }

    private func summaries(component: Calendar.Component, limit: Int) -> [SpendingSummary] {
        let grouped = Dictionary(grouping: expenses) { expense in
            calendar.dateInterval(of: component, for: expense.createdAt)?.start ?? expense.createdAt
        }

        return grouped
            .map { startDate, expenses in
                SpendingSummary(
                    id: startDate,
                    title: summaryTitle(for: startDate, component: component),
                    detail: summaryDetail(for: startDate, component: component),
                    amount: expenses.reduce(Decimal.zero) { $0 + $1.amount }
                )
            }
            .sorted { $0.id > $1.id }
            .prefix(limit)
            .map { $0 }
    }

    private func summaryTitle(for startDate: Date, component: Calendar.Component) -> String {
        switch component {
        case .weekOfYear:
            if calendar.isDate(Date(), equalTo: startDate, toGranularity: .weekOfYear) {
                return "This week"
            }

            return "Week of \(Formatters.shortDate.string(from: startDate))"
        case .month:
            if calendar.isDate(Date(), equalTo: startDate, toGranularity: .month) {
                return "This month"
            }

            return Formatters.month.string(from: startDate)
        default:
            return Formatters.shortDate.string(from: startDate)
        }
    }

    private func summaryDetail(for startDate: Date, component: Calendar.Component) -> String {
        guard let interval = calendar.dateInterval(of: component, for: startDate) else {
            return ""
        }

        let endDate = calendar.date(byAdding: .day, value: -1, to: interval.end) ?? interval.end

        switch component {
        case .weekOfYear:
            return "\(Formatters.shortDate.string(from: startDate)) - \(Formatters.shortDate.string(from: endDate))"
        case .month:
            return Formatters.year.string(from: startDate)
        default:
            return ""
        }
    }
}

struct SpendingSummary: Identifiable, Equatable {
    let id: Date
    let title: String
    let detail: String
    let amount: Decimal
}

enum ExpenseStorage {
    private static let storageKey = "spent.expenses.v1"
    private static let appGroupIdentifier = "group.com.annabelfilippini.spent"

    static func load() -> [Expense] {
        migrateStandardStorageIfNeeded()

        guard let data = sharedDefaults.data(forKey: storageKey) else {
            return []
        }

        do {
            return try JSONDecoder().decode([Expense].self, from: data)
        } catch {
            return []
        }
    }

    static func save(_ expenses: [Expense]) {
        do {
            let data = try JSONEncoder().encode(expenses)
            sharedDefaults.set(data, forKey: storageKey)
            WidgetCenter.shared.reloadAllTimelines()
        } catch {
            assertionFailure("Unable to save expenses.")
        }
    }

    static func add(amount: Decimal, item: String) {
        let cleanedItem = item.trimmingCharacters(in: .whitespacesAndNewlines)
        guard amount > 0, !cleanedItem.isEmpty else {
            return
        }

        var expenses = load()
        expenses.append(Expense(amount: amount, item: cleanedItem))
        save(expenses)
    }

    private static var sharedDefaults: UserDefaults {
        UserDefaults(suiteName: appGroupIdentifier) ?? .standard
    }

    private static func migrateStandardStorageIfNeeded() {
        guard sharedDefaults.data(forKey: storageKey) == nil,
              let standardData = UserDefaults.standard.data(forKey: storageKey) else {
            return
        }

        sharedDefaults.set(standardData, forKey: storageKey)
    }
}
