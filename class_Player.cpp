#include <vector>

class Player {
public:
    std::vector<Domino> hand;
    std::string name;

    Player(std::string playerName) : name(playerName) {}

    // Add a piece to the player's hand
    void addDomino(const Domino& domino) {
        hand.push_back(domino);
    }

    // Find and return a playable piece based on the current table head or tail
    Domino* findMatchingPiece(int head, int tail) {
        for (auto& domino : hand) {
            if (domino.canMatch(head) || domino.canMatch(tail)) {
                return &domino;
            }
        }
        return nullptr; // No matching piece found
    }

    // Remove a domino from the hand after playing
    void removeDomino(Domino* domino) {
        hand.erase(std::remove(hand.begin(), hand.end(), *domino), hand.end());
    }

    bool hasNoPieces() const {
        return hand.empty();
    }
};
