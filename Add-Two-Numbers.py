class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry: # listas podem ter tamanho diferente
            v1 = l1.val if l1 else 0 # Atribui 0 caso o valor seja nulo
            v2 = l2.val if l2 else 0 # Atribui 0 caso o valor seja nulo

            total = v1 + v2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next # avança o ptr

            if l1:
                l1 = l1.next # avança o ptr da l1

            if l2:
                l2 = l2.next # avança o ptr da l1

        return dummy.next
