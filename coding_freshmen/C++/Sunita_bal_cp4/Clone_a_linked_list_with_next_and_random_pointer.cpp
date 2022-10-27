class Solution{
{
    private:
    void insertAtTail(Node* &head, Node* &tail, int val){
        Node* newNode = new Node(val);
        if(head == NULL){
            head = newNode;
            tail = newNode;
            return;
        }
        else{
            tail -> next = newNode;
            tail = newNode;
        }
    }
    public:
    Node *copyList(Node *head)
    {
        //Write your code here
        Node* cloneHead = NULL;
        Node* cloneTail = NULL;
        
        Node* temp = head;
        
        while(temp != NULL){
            insertAtTail(cloneHead,cloneTail,temp -> data);
            temp = temp -> next;
        }
        
           Node* originalNode=head;

       Node* cloneNode=cloneHead;

       while(originalNode!=NULL && cloneNode!=NULL){

           Node* next=originalNode->next;
           originalNode->next=cloneNode;
           originalNode=next;

           next=cloneNode->next;
           cloneNode->next=originalNode; 
           cloneNode=next;
       } 
       
        temp=head; 
       while(temp!=NULL){
           
          if(temp->next!=NULL){
              
              temp->next->arb=temp->arb?temp->arb->next:temp->arb;
          }
          
          temp=temp->next->next;

       }
       

       originalNode=head;
       cloneNode=cloneHead;
       
        while(originalNode!=NULL && cloneNode!=NULL){

           originalNode->next=cloneNode->next;
           originalNode=originalNode->next;
           
           if(originalNode!=NULL){

           cloneNode->next=originalNode->next;

           }

           cloneNode=cloneNode->next;

       }

      

       return cloneHead;
       
    }

};