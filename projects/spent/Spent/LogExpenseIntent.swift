import AppIntents
import Foundation

struct LogExpenseIntent: AppIntent {
    static let title: LocalizedStringResource = "Log Expense"
    static let description = IntentDescription("Save an amount and item to Spent.")
    static let openAppWhenRun = false

    @Parameter(title: "Amount")
    var amount: Double

    @Parameter(title: "Item")
    var item: String

    func perform() async throws -> some IntentResult & ProvidesDialog {
        let cleanedItem = item.trimmingCharacters(in: .whitespacesAndNewlines)
        guard amount > 0, !cleanedItem.isEmpty, cleanedItem != "Ask Each Time" else {
            return .result(dialog: "This did not save. The shortcut needs an amount and item.")
        }

        let decimalAmount = Decimal(amount)
        ExpenseStorage.add(amount: decimalAmount, item: cleanedItem)

        let formattedAmount = Formatters.currencyString(decimalAmount)
        return .result(dialog: "Saved \(formattedAmount) for \(cleanedItem).")
    }
}

struct SpentShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: LogExpenseIntent(),
            phrases: [
                "Log an expense in \(.applicationName)",
                "Add a purchase to \(.applicationName)",
                "Save spending in \(.applicationName)"
            ],
            shortTitle: "Log Expense",
            systemImageName: "plus.circle"
        )
    }
}
