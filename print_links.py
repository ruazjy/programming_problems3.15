#coding:utf-8
#从尾到头打印单链表
#方法一：使用栈
def print_links(links):
    stack=[]
    while links:
        stack.append(links.val)
        links=links.next
    while stack:
        print stack.pop()
#方法二：直接递归
def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print links.val

