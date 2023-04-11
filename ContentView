import SwiftUI

struct ContentView: View {
    @State var paragraphText = "Hey how are you"
    @State var questionText = ""

    var body: some View {
        VStack {
            Text("App")
                .padding()
                .background(Color.gray)
                .cornerRadius(10)
            
            TextEditor(text: $paragraphText)
                .frame(height: 200)
                .padding()
                .background(Color.gray)
                .cornerRadius(10)
            
            Button(action: {
                generateQuestions()
            }) {
                Text("Generate Questions")
            }
            
            Spacer()
            
            if !questionText.isEmpty {
                Text("Generated question:")
                    .padding()
                    .background(Color.gray)
                    .cornerRadius(10)
                
                Text(questionText)
                    .padding()
                    .background(Color.gray)
                    .cornerRadius(10)
            }
        }
        .padding()
    }
    
    private func generateQuestions() {
        let apiKey = "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"
        let prompt = paragraphText
        let urlString = "https://api.openai.com/v1/engines/davinci-codex/completions"
        let headers = [
            "Content-Type": "application/json",
            "Authorization": "Bearer \(apiKey)"
        ]
        let parameters : [String : Any] = [
            "prompt": prompt,
            "max_tokens": 5,
            "temperature": 0.7
        ]
        
        let url = URL(string: urlString)!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.allHTTPHeaderFields = headers
        request.httpBody = try? JSONSerialization.data(withJSONObject: parameters)
        
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            if error != nil {
                print("Error making API request: \(error!.localizedDescription)")
                return
            }
            
            if let data = data, let json = try? JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] {
                if let choices = json["choices"] as? [[String: Any]], let text = choices.first?["text"] as? String {
                    DispatchQueue.main.async {
                        questionText = text
                    }
                }
            }
        }
        
        task.resume()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
