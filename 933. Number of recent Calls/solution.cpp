class RecentCounter {
public:
    RecentCounter() {}

    int ping(int t) {
        while (!requests.empty() && requests.front() < t - 3000) {
            requests.pop();
        }
        requests.push(t);
        return requests.size();
    }

private:
    std::queue<int> requests;
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */