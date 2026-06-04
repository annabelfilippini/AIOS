import Foundation

struct Expense: Identifiable, Codable, Equatable {
    let id: UUID
    var amount: Decimal
    var item: String
    let createdAt: Date

    init(id: UUID = UUID(), amount: Decimal, item: String, createdAt: Date = Date()) {
        self.id = id
        self.amount = amount
        self.item = item
        self.createdAt = createdAt
    }
}

extension Decimal {
    var doubleValue: Double {
        NSDecimalNumber(decimal: self).doubleValue
    }
}

