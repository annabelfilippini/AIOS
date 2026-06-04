import SwiftUI

struct HomeView: View {
    @EnvironmentObject private var store: ExpenseStore
    @FocusState private var focusedField: Field?

    @State private var amountText = ""
    @State private var itemText = ""
    @State private var showSavePulse = false

    private enum Field {
        case amount
        case item
    }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 18) {
                    header
                    entryPanel
                    totals
                    recentList
                    summarySections
                }
                .padding(.horizontal, 20)
                .padding(.top, 12)
                .padding(.bottom, 90)
            }
            .scrollIndicators(.visible)
            .background(Color.spentBackground.ignoresSafeArea())
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .principal) {
                    Text("Spent")
                        .font(.system(size: 17, weight: .semibold, design: .rounded))
                }
            }
            .onAppear {
                store.reloadFromStorage()
                focusedField = .amount
            }
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Quick add")
                .font(.system(size: 28, weight: .bold, design: .rounded))
                .frame(maxWidth: .infinity, alignment: .leading)

            Text("Amount and item. That is the whole thing.")
                .font(.system(size: 14, weight: .regular, design: .rounded))
                .foregroundStyle(.secondary)
        }
    }

    private var entryPanel: some View {
        VStack(spacing: 10) {
            HStack(alignment: .firstTextBaseline, spacing: 8) {
                Text("$")
                    .font(.system(size: 28, weight: .semibold, design: .rounded))
                    .foregroundStyle(.secondary)

                TextField("0.00", text: $amountText)
                    .keyboardType(.decimalPad)
                    .focused($focusedField, equals: .amount)
                    .font(.system(size: 34, weight: .bold, design: .rounded))
                    .textInputAutocapitalization(.never)
            }

            TextField("What did you buy?", text: $itemText)
                .focused($focusedField, equals: .item)
                .font(.system(size: 19, weight: .medium, design: .rounded))
                .submitLabel(.done)
                .padding(13)
                .background(Color.white)
                .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
                .overlay(
                    RoundedRectangle(cornerRadius: 8, style: .continuous)
                        .stroke(Color.spentLine, lineWidth: 1)
                )

            Button {
                saveExpense()
            } label: {
                Label("Save purchase", systemImage: "checkmark")
                    .font(.system(size: 17, weight: .semibold, design: .rounded))
                    .frame(maxWidth: .infinity)
                    .frame(height: 48)
            }
            .buttonStyle(.plain)
            .foregroundStyle(.white)
            .background(canSave ? Color.black : Color.spentMuted)
            .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
            .scaleEffect(showSavePulse ? 0.98 : 1)
            .disabled(!canSave)
            .animation(.snappy(duration: 0.18), value: canSave)
            .animation(.snappy(duration: 0.12), value: showSavePulse)
        }
        .padding(14)
        .background(Color.spentPanel)
        .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
        .overlay(
            RoundedRectangle(cornerRadius: 8, style: .continuous)
                .stroke(Color.spentLine, lineWidth: 1)
        )
    }

    private var totals: some View {
        HStack(spacing: 12) {
            TotalTile(title: "Today", amount: store.todayTotal)
            TotalTile(title: "This month", amount: store.monthTotal)
        }
    }

    private var summarySections: some View {
        VStack(spacing: 18) {
            SummarySection(title: "Weeks", summaries: store.weeklySummaries)
            SummarySection(title: "Months", summaries: store.monthlySummaries)
        }
    }

    private var recentList: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Recent")
                .font(.system(size: 20, weight: .bold, design: .rounded))

            if store.recentExpenses.isEmpty {
                EmptyState()
            } else {
                VStack(spacing: 0) {
                    ForEach(store.recentExpenses) { expense in
                        ExpenseRow(expense: expense) {
                            store.delete(expense)
                        }

                        if expense.id != store.recentExpenses.last?.id {
                            Divider()
                                .padding(.leading, 14)
                        }
                    }
                }
                .background(Color.white)
                .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
                .overlay(
                    RoundedRectangle(cornerRadius: 8, style: .continuous)
                        .stroke(Color.spentLine, lineWidth: 1)
                )
            }
        }
    }

    private var canSave: Bool {
        parsedAmount != nil && !itemText.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }

    private var parsedAmount: Decimal? {
        Decimal(string: amountText.replacingOccurrences(of: ",", with: ""))
    }

    private func saveExpense() {
        guard let amount = parsedAmount else {
            return
        }

        store.add(amount: amount, item: itemText)
        amountText = ""
        itemText = ""
        focusedField = .amount

        showSavePulse = true
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.12) {
            showSavePulse = false
        }
    }
}

private struct TotalTile: View {
    let title: String
    let amount: Decimal

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(title)
                .font(.system(size: 14, weight: .medium, design: .rounded))
                .foregroundStyle(.secondary)

            Text(Formatters.currencyString(amount))
                .font(.system(size: 22, weight: .bold, design: .rounded))
                .lineLimit(1)
                .minimumScaleFactor(0.75)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(16)
        .background(Color.white)
        .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
        .overlay(
            RoundedRectangle(cornerRadius: 8, style: .continuous)
                .stroke(Color.spentLine, lineWidth: 1)
        )
    }
}

private struct ExpenseRow: View {
    let expense: Expense
    let onDelete: () -> Void

    var body: some View {
        HStack(spacing: 14) {
            VStack(alignment: .leading, spacing: 4) {
                Text(expense.item)
                    .font(.system(size: 16, weight: .semibold, design: .rounded))
                    .lineLimit(1)

                Text(Formatters.time.string(from: expense.createdAt))
                    .font(.system(size: 13, weight: .medium, design: .rounded))
                    .foregroundStyle(.secondary)
            }

            Spacer(minLength: 12)

            Text(Formatters.currencyString(expense.amount))
                .font(.system(size: 16, weight: .bold, design: .rounded))
                .lineLimit(1)
                .minimumScaleFactor(0.8)

            Button(action: onDelete) {
                Image(systemName: "xmark")
                    .font(.system(size: 12, weight: .bold))
                    .foregroundStyle(.secondary)
                    .frame(width: 28, height: 28)
                    .background(Color.spentBackground)
                    .clipShape(Circle())
            }
            .buttonStyle(.plain)
            .accessibilityLabel("Delete \(expense.item)")
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 13)
    }
}

private struct SummarySection: View {
    let title: String
    let summaries: [SpendingSummary]

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(title)
                .font(.system(size: 20, weight: .bold, design: .rounded))

            if summaries.isEmpty {
                SummaryEmptyState(title: "No \(title.lowercased()) yet")
            } else {
                VStack(spacing: 0) {
                    ForEach(summaries) { summary in
                        SummaryRow(summary: summary)

                        if summary.id != summaries.last?.id {
                            Divider()
                                .padding(.leading, 14)
                        }
                    }
                }
                .background(Color.white)
                .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
                .overlay(
                    RoundedRectangle(cornerRadius: 8, style: .continuous)
                        .stroke(Color.spentLine, lineWidth: 1)
                )
            }
        }
    }
}

private struct SummaryRow: View {
    let summary: SpendingSummary

    var body: some View {
        HStack(spacing: 14) {
            VStack(alignment: .leading, spacing: 4) {
                Text(summary.title)
                    .font(.system(size: 16, weight: .semibold, design: .rounded))
                    .lineLimit(1)

                if !summary.detail.isEmpty {
                    Text(summary.detail)
                        .font(.system(size: 13, weight: .medium, design: .rounded))
                        .foregroundStyle(.secondary)
                }
            }

            Spacer(minLength: 12)

            Text(Formatters.currencyString(summary.amount))
                .font(.system(size: 16, weight: .bold, design: .rounded))
                .lineLimit(1)
                .minimumScaleFactor(0.8)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 13)
    }
}

private struct SummaryEmptyState: View {
    let title: String

    var body: some View {
        Text(title)
            .font(.system(size: 15, weight: .medium, design: .rounded))
            .foregroundStyle(.secondary)
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(16)
            .background(Color.white)
            .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
            .overlay(
                RoundedRectangle(cornerRadius: 8, style: .continuous)
                    .stroke(Color.spentLine, lineWidth: 1)
            )
    }
}

private struct EmptyState: View {
    var body: some View {
        VStack(spacing: 8) {
            Image(systemName: "receipt")
                .font(.system(size: 26, weight: .regular))
                .foregroundStyle(.secondary)

            Text("No purchases yet")
                .font(.system(size: 17, weight: .semibold, design: .rounded))

            Text("Your first saved item will show up here.")
                .font(.system(size: 14, weight: .regular, design: .rounded))
                .foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 34)
        .background(Color.white)
        .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
        .overlay(
            RoundedRectangle(cornerRadius: 8, style: .continuous)
                .stroke(Color.spentLine, lineWidth: 1)
        )
    }
}

private extension Color {
    static let spentBackground = Color(red: 0.973, green: 0.973, blue: 0.965)
    static let spentPanel = Color(red: 0.996, green: 0.996, blue: 0.992)
    static let spentLine = Color(red: 0.88, green: 0.875, blue: 0.855)
    static let spentMuted = Color(red: 0.70, green: 0.70, blue: 0.68)
}

#Preview {
    HomeView()
        .environmentObject(ExpenseStore())
}
