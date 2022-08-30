
import Vue from 'vue';

//import VoerroTagsInput from '@voerro/vue-tagsinput';
//Vue.component('tags-input', VoerroTagsInput);

Vue.filter('spaceBetweenNum', (price)=>{ 
	price += "";
	var pattern = /(-?\d+)(\d{3})/;
	while (pattern.test(price))
		price = price.replace(pattern, "$1 $2");
	return price; 
})


Vue.filter('textLimit', (text, count)=>{ 
  if( text.length > count*1 ){
    text = text.substring(0, count )
    text = text+ " ...";
  }
	return text; 
})
