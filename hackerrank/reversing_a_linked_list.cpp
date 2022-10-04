#include <bits/stdc++.h>

using namespace std;
class LinkedListNode {
public:
    int val;
    LinkedListNode *next;

    LinkedListNode(int node_value) {
        val = node_value;
        next = NULL;
    }
};

LinkedListNode* _insert_node_into_singlylinkedlist(LinkedListNode *head, LinkedListNode *tail, int val) {
    if(head == NULL) {
        head = new LinkedListNode(val);
        tail = head;
    }
    else {
        LinkedListNode *node = new LinkedListNode(val);
        tail->next = node;
        tail = tail->next;
    }
    return tail;
}

/*
 * Complete the function below.
 */
/*
For your reference:
LinkedListNode {
    int val;
    LinkedListNode *next;
};
*/
LinkedListNode* LL(LinkedListNode* l) {
    LinkedListNode* n = NULL;
    LinkedListNode* p = NULL;
    while (l != NULL) {
        n = l->next;
        l->next = p;
        
        p = l;
        l = n;
    }
    
    return p;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    LinkedListNode* res;
    int l_size = 0;

    LinkedListNode* l = NULL;
    LinkedListNode* l_tail = NULL;

    cin >> l_size;

    for(int i = 0; i < l_size; i++) {
        int l_item;
        cin >> l_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        l_tail = _insert_node_into_singlylinkedlist(l, l_tail, l_item);

        if(i == 0) {
            l = l_tail;
        }
    }


    res = LL(l);
    while (res != NULL) {
        fout << res->val << endl;

        res = res->next;
    }

    fout.close();
    return 0;
}
