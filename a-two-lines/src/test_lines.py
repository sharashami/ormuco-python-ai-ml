import unittest
import lines

class TestLines(unittest.TestCase):

    def test_overlap(self):
        #int
        self.assertEqual(lines.overlap(1,5,5,6), True) 
        self.assertEqual(lines.overlap(5,1,6,5), True)#unordered   
        self.assertEqual(lines.overlap(6,5,5,1), True)#unordered
        self.assertEqual(lines.overlap(1,5,2,6), True) 
        self.assertEqual(lines.overlap(5,1,6,2), True)#unordered      
        self.assertEqual(lines.overlap(2,6,1,5), True)#unordered
        self.assertEqual(lines.overlap(6,2,5,1), True)   
        self.assertEqual(lines.overlap(1,5,6,8), False) 
        self.assertEqual(lines.overlap(5,1,8,6), False)#unordered
        self.assertEqual(lines.overlap(6,8,1,5), False)
        self.assertEqual(lines.overlap(8,6,5,1), False)#unordered
        #float
        self.assertEqual(lines.overlap(1.3,5.3,2.3,6.3), True)        
        self.assertEqual(lines.overlap(2.3,6.3,1.3,5.3), True)
        self.assertEqual(lines.overlap(1.3,5.3,6.3,8.3), False)
        self.assertEqual(lines.overlap(6.3,8.3,1.3,5.3), False)
        #negative
        self.assertEqual(lines.overlap(-3,0,-2,6), True)        
        self.assertEqual(lines.overlap(-2,6,-3,0), True)
        self.assertEqual(lines.overlap(-7,-2,-1,5), False)
        self.assertEqual(lines.overlap(-1,5,-7,-2), False)

        with self.assertRaises(ValueError):
            lines.overlap(6,6,1,5)#a line cannot have same start and end value
        with self.assertRaises(ValueError):
            lines.overlap(1,5,6,6)    
        with self.assertRaises(ValueError):
            lines.overlap('f',5,6,6)  

if __name__ == '__main__':
    unittest.main()