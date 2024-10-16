class Domino {
public:
    int left;
    int right;
    bool isPlayed;  // To track if the piece has been played

    Domino(int leftSide, int rightSide) : left(leftSide), right(rightSide), isPlayed(false) {}

    // Optional: Helper function to check if the piece can match the chain
    bool canMatch(int value) {
        return left == value || right == value;
    }

    void markPlayed() {
        isPlayed = true;
    }
};
