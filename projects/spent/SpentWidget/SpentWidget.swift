import SwiftUI
import WidgetKit

struct SpentWidgetEntry: TimelineEntry {
    let date: Date
    let weekTotal: Decimal
    let monthTotal: Decimal
    let recentItem: String?
}

struct SpentWidgetProvider: TimelineProvider {
    func placeholder(in context: Context) -> SpentWidgetEntry {
        SpentWidgetEntry(date: Date(), weekTotal: 42.50, monthTotal: 210.75, recentItem: "coffee")
    }

    func getSnapshot(in context: Context, completion: @escaping (SpentWidgetEntry) -> Void) {
        completion(entry())
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<SpentWidgetEntry>) -> Void) {
        let nextRefresh = Calendar.current.date(byAdding: .minute, value: 30, to: Date()) ?? Date()
        completion(Timeline(entries: [entry()], policy: .after(nextRefresh)))
    }

    private func entry() -> SpentWidgetEntry {
        let expenses = ExpenseStorage.load()
        let calendar = Calendar.current
        let now = Date()

        let weekTotal = expenses
            .filter { calendar.isDate($0.createdAt, equalTo: now, toGranularity: .weekOfYear) }
            .reduce(Decimal.zero) { $0 + $1.amount }

        let monthTotal = expenses
            .filter { calendar.isDate($0.createdAt, equalTo: now, toGranularity: .month) }
            .reduce(Decimal.zero) { $0 + $1.amount }

        let recentItem = expenses
            .sorted { $0.createdAt > $1.createdAt }
            .first?
            .item

        return SpentWidgetEntry(date: now, weekTotal: weekTotal, monthTotal: monthTotal, recentItem: recentItem)
    }
}

struct SpentWidgetView: View {
    let entry: SpentWidgetEntry

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                Text("Spent")
                    .font(.system(size: 15, weight: .bold, design: .rounded))

                Spacer()

                Image(systemName: "plus.circle.fill")
                    .font(.system(size: 18, weight: .semibold))
            }

            VStack(alignment: .leading, spacing: 3) {
                Text("This week")
                    .font(.system(size: 12, weight: .medium, design: .rounded))
                    .foregroundStyle(.secondary)

                Text(Formatters.currencyString(entry.weekTotal))
                    .font(.system(size: 24, weight: .bold, design: .rounded))
                    .lineLimit(1)
                    .minimumScaleFactor(0.75)
            }

            HStack {
                Text("Month")
                    .font(.system(size: 12, weight: .medium, design: .rounded))
                    .foregroundStyle(.secondary)

                Spacer()

                Text(Formatters.currencyString(entry.monthTotal))
                    .font(.system(size: 13, weight: .bold, design: .rounded))
                    .lineLimit(1)
                    .minimumScaleFactor(0.75)
            }

            if let recentItem = entry.recentItem {
                Text(recentItem)
                    .font(.system(size: 11, weight: .medium, design: .rounded))
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
            }
        }
        .containerBackground(Color.white, for: .widget)
        .widgetURL(URL(string: "spent://add"))
    }
}

@main
struct SpentWidget: Widget {
    let kind = "SpentWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: SpentWidgetProvider()) { entry in
            SpentWidgetView(entry: entry)
        }
        .configurationDisplayName("Spent")
        .description("See this week's spending at a glance.")
        .supportedFamilies([.systemSmall])
    }
}
