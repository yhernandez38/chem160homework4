class point:
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum

    def add(self, p2):
        add = 0

        for i in range(self.dim):
            add = self.data[i]+p2.data[i]
        
            

    def sqmag(self,newp1):
        sqmag = 0

        for i in range(self.dim):
            sqmag = (self.data[i])**2 + (newp1.data[1])**2

        return sqmag
