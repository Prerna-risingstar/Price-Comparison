#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Product {
    string site;
    int price;
    double rating;
};

int main() {
    cout << "=== 🚀 CPP Price Comparison ===\n\n";
    
    vector<Product> products = {
        {"Amazon", 49999, 4.5},
        {"Flipkart", 48999, 4.3},
        {"Myntra", 51999, 4.2},
        {"Croma", 47999, 4.6}
    };
    
    int minPrice = 999999;
    string bestSite;
    
    for(auto& p : products) {
        cout << "💰 " << left << setw(10) << p.site 
             << "Rs " << setw(8) << p.price 
             << "⭐ " << fixed << setprecision(1) << p.rating << endl;
        
        if(p.price < minPrice) {
            minPrice = p.price;
            bestSite = p.site;
        }
    }
    
    cout << "\n🏆 BEST DEAL: " << bestSite << " - Rs " << minPrice << endl;
    cout << "Press Enter to exit...";
    cin.get();
    return 0;
}