def find_integer(matrix,num):
    '''
    :param matrix:[[]] 
    :param num:int 
    :return: bool
    '''
    if not matrix:
        return False
    rows,cols=len(matrix),len(matrix[0])
    row,col=0,cols-1
    while row<rows and col>=0:
        if num==matrix[row][col]:
            return True
        elif num>matrix[row][col]:
            row+=1
        else :
            col-=1
    return  False
