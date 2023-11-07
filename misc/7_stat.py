#!/usr/local/bin
import unittest




def compute(definitions,data):
    result = {}

    for k in definitions.keys():
        result[k] = [0] * 7

    # loop through every piece of data

    for channel in data.keys():
        week = data[channel]
            
        
        for report_category in definitions.keys():
            if channel in definitions[report_category]:
                for i in range(0,  len(result[report_category])):
                    result[report_category][i] +=week[i]
    
    for k in result.keys():
        result[k] = sum(list(map(lambda x: min(1,x), result[k])))
    

    

    return result

        

class testCase(unittest.TestCase):
    def test_happy_case(self):
        
        definitions  = { }
        definitions['overall'] = ['web', 'mobile', 'iphone']
        definitions['mobile'] = ['iphone', 'android']
                

        data = { }
        data['iphone'] =  [1,0,1,0,1,0,0]
        data['web'] =     [1,1,1,0,0,0,1]
        data['android'] = [1,1,0,0,0,0,0]
        
        result = compute(definitions,data)

        self.assertEqual(result['overall'], 5)
        self.assertEqual(result['mobile'], 4)
        
        result = compute (definitions,{})
        self.assertEqual(result['overall'], 0)

if __name__=="__main__":
    unittest.main().result
