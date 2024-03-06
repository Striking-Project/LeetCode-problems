/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }        

        ListNode* odd_head = head;
        ListNode* even_head = head->next;
        ListNode* odd_tail = odd_head;
        ListNode* even_tail = even_head;

        while (even_tail && even_tail->next) {
            odd_tail->next = even_tail->next;
            odd_tail = odd_tail->next;
            even_tail->next = odd_tail->next;
            even_tail = even_tail->next;
        }

        odd_tail->next = even_head;

        return odd_head;
    }
};