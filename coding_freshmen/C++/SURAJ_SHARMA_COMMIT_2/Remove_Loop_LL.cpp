struct Node
{
    int data;
    Node* next;
    
    Node(int val)
    {
        data = val;
        next = NULL;
    }
};

*/

class Solution
{   private:
    Node* inter(Node* head){
           // your code here
           if(head==NULL){
               return NULL;
           }
        Node* slow=head;
        Node* fast=head;
        while(slow!=NULL&&fast!=NULL){
            slow=slow->next;
            fast=fast->next;
             if(fast==NULL){
                 return NULL;
             }
            fast=fast->next;
            if(fast==slow){
                return slow;
            }
        }
        
    }
    public:
    //Function to remove a loop in the linked list.
    void removeLoop(Node* head)
    {
        // code here
        // just remove the loop without losing any nodes
        Node* intersection=inter(head);
 if(intersection==NULL){
     return;
 }
        Node* slow=head;
        
        while(slow!=intersection){
            slow=slow->next;
            intersection=intersection->next;
        }
        Node* beginn=slow;
        while(beginn->next!=slow){
            beginn=beginn->next;
        }
        beginn->next=NULL;
    }
};