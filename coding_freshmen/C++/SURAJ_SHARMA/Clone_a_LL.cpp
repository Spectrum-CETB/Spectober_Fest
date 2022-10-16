{ private:
    void insertAtTail(Node* &head,Node* &tail,int data){
        Node* temp=new Node(data);
        if(head==NULL){
            head=temp;
            tail=temp;
        }
        else{
            tail->next=temp;
            tail=temp;
        }
    }
    public:
    Node *copyList(Node *head)
    //step-1 copy the original LL
    {
        //Write your code here
         Node* clonehead=NULL;
        Node* clonetail=NULL;
    
       Node* temp=head; 
        while(temp!=NULL){
            insertAtTail(clonehead,clonetail,temp->data);
            temp=temp->next;
       
    }
    //step-2 ulat plat
    Node* original=head;
    Node* clone=clonehead;
    while(original!=NULL&&clone!=NULL){
        
    Node* next=original->next;
    original->next=clone;
    original=next;
    next=clone->next;
    clone->next=original;
    clone=next;
    
    }
    //step-3 random set krdo
    temp=head;
    while(temp!=NULL){
        if(temp->next!=NULL){
            if(temp->arb!=NULL){
                
            temp->next->arb=temp->arb->next;
            
            }
            else{
                temp->next->arb=NULL;
            }
        }
        temp=temp->next->next;
        
    }
    //ulat palat ko theek kr do
    original=head;
    clone=clonehead;
    while(original!=NULL&&clone!=NULL){
        
    original->next=clone->next;
    original=clone->next;
    if(original!=NULL){
        clone->next=original->next;
    }
    clone=clone->next;
    
    }
    return clonehead;
    }
    
 
};