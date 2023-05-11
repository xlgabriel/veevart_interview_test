public class main {

    static void start(){
        
        List<Elements> elements = new List<Elements>();
        
        Integer maxcapacity = Integer.valueof((Math.random() * 5) + 15);
        Backpack bp = new Backpack(maxcapacity);
        
        for(Integer i = 0; i < Integer.valueof((Math.random() * 4) + 4); i++ ){
			Integer randomnum = Integer.valueof((Math.random() + 10));
            elements.add(new Elements(randomnum, randomnum + 1));
        }
        
        System.debug('Elements: ' + elements);
		System.debug('Max capacity: ' + maxcapacity);
		System.debug('Backpack and total price respectively');
        
        Backpack backpack = process(0, elements, bp);
		System.debug(backpack.elements + 'value: ' + backpack.value);
        
    }
    
    static Backpack process(Integer i, List<Elements> elements, Backpack backpack)
    {
        if (i >= elements.size()){
			return backpack;
        }
        else
        {
        
            if(backpack.w_max - elements[i].weight < 0){
                return process(i + 1, elements, backpack);	
            }
            else
            {
                Backpack answer1 = process(i + 1, elements, backpack);
                backpack.value += elements[i].value;
                backpack.elements.add(elements[i]);
                backpack.w_max = backpack.w_max - elements[i].weight;
                Backpack answer2 = process(i + 1, elements, backpack);
                
                if (answer1.value > answer2.value){
                    return answer1;
                }
                else
                {
                    return answer2;             
                }
    
            }
        
            
        }
        
    }
    
}