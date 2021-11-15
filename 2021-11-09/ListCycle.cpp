
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        bool b = false; // returned
        ListNode* temp = head; // initial
        if (temp == nullptr) {
            return false;
        } // if head is null to begin with
        while (temp->next != nullptr) {
            if (temp->val == 1000001) {
                b = true;
                break;
            } // if we visited this node twice
            temp->val = 1000001; // val cannot be this value as per this problem's contraints
            temp = temp->next; // although this modifies the list irreversibly
        } // while next one is not null
        return b;
    } // time complexity of O(n), space complexity of O(1)
};