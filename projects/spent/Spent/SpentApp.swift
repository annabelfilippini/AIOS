import SwiftUI

@main
struct SpentApp: App {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var store = ExpenseStore()

    var body: some Scene {
        WindowGroup {
            HomeView()
                .environmentObject(store)
        }
        .onChange(of: scenePhase) { _, newPhase in
            if newPhase == .active {
                store.reloadFromStorage()
            }
        }
    }
}
