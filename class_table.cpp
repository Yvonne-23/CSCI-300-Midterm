#include <deque> // To manage the domino chain

class Table {
public:
    std::deque<Domino> dominoChain; // To store the domino pieces played
    std::vector<Domino> availablePieces; // Pieces not yet picked up

    void addDominoToChain(const Domino& domino, bool toHead) {
        if (toHead) {
            dominoChain.push_front(domino);  // Add to the head
        } else {
            dominoChain.push_back(domino);   // Add to the tail
        }
    }

    int getHeadValue() const {
        return dominoChain.front().left; // Get the left value of the first domino in the chain
    }

    int getTailValue() const {
        return dominoChain.back().right; // Get the right value of the last domino in the chain
    }

    void initializeAvailablePieces() {
        for (int i = 0; i <= 6; ++i) {
            for (int j = i; j <= 6; ++j) {
                availablePieces.push_back(Domino(i, j));
            }
        }
    }
};
