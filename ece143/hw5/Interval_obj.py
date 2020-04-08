class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b
    def __repr__(self):
        '''
        __repr__ funtion
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        return "Interval({},{})".format(self._a, self._b)
    def __eq__(self,other):
        '''
        responds to '=='
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        assert isinstance(other._a,int)
        assert isinstance(other._b,int)
        return self._a == other._a and self._b == other._b
    def __lt__(self,other):
        '''
        responds to '<'
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        assert isinstance(other._a,int)
        assert isinstance(other._b,int)
        return self._b<other._a
    def __gt__(self,other):
        '''
        responds to '>'
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        assert isinstance(other._a,int)
        assert isinstance(other._b,int)
        return self._b>other._a
    def __ge__(self,other):
        '''
        responds to '>='
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        assert isinstance(other._a,int)
        assert isinstance(other._b,int)
        return self._a>=other._b
    def __le__(self,other):
        '''
        responds to '<='
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        assert isinstance(other._a,int)
        assert isinstance(other._b,int)
        return self._a<=other._b
    def __add__(self,other):
        '''
        responds to '+'
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        assert isinstance(other._a,int)
        assert isinstance(other._b,int)
        if(self.isIntersecting(other)):
            return Interval(min(self._a, other._a), max(self._b, other._b))
        else:
            return [Interval(self._a, self._b), Interval(other._a,other._b)]

    def isIntersecting(self, other):
        '''
        returns true if the two intervals are intersecting
        '''
        assert isinstance(self._a,int)
        assert isinstance(self._b,int)
        assert isinstance(other._a,int)
        assert isinstance(other._b,int)
        if(other._a<=self._a):
            if(other._b>self._a):
                return True
            else:
                return False
        elif self._a<other._a and other._a<self._b:
                return True
        else:
            return False
