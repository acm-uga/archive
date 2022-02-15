struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) {
            return l2;
        } else if (l2 == nullptr) {
            return l1;
        }
        if (l2->val < l1->val) {
            ListNode* temp = l2;
            l2 = l2->next;
            temp->next = l1;
            l1 = temp;
        }
        ListNode* head = l1;
        if (l2 == nullptr) {
            return head;
        }
        while(l1->next != nullptr && l2->next != nullptr) {
            if (l1->val > l2->val) {
                ListNode* temp = l1;
                l1 = l1->next;
                ins(temp, l2);
                l2 = l2->next;
            } else {
                if (l1->next->val > l2->val) {
                    ListNode* temp = l2;
                    l2 = l2->next;
                    ins(temp, l1);
                    l1 = l1->next;
                } else {
                    l1 = l1->next;
                }
            }
        }
        if (l1->next == nullptr) {
            l1->next = l2;
        } else {
            while (l1->next != nullptr && l1->next->val < l2->val) {
                l1 = l1->next;
            }
            ins(l2,l1);
        }
        return head;
    }
    
    void ins(ListNode* l1, ListNode* l2) {
        l1->next = l2->next;
        l2->next = l1;
    }
};