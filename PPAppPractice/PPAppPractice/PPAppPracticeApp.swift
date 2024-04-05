//
//  PPAppPracticeApp.swift
//  PPAppPractice
//
//  Created by Shriyan Gote on 4/3/24.
//

// PPAppPracticeApp.swift
// PPAppPracticeApp.swift
import SwiftUI

@main
struct PPAppPracticeApp: App {
    // Add a state variable to track the user's authentication status
    @State private var isAuthenticated = false

    var body: some Scene {
        WindowGroup {
            if isAuthenticated {
                ContentView() // Display the main view if authenticated
            } else {
                LoginView(isAuthenticated: $isAuthenticated) // Pass isAuthenticated binding to LoginView
            }
        }
    }
}


