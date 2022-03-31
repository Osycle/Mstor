import Vue from 'vue';
import {VueEditor, Quill} from "vue2-editor";
import { ImageDrop } from 'quill-image-drop-module'
// import { ImageResize } from 'quill-image-resize-module';


// import {Quill} from "vue2-editor";
window.Quill = Quill
// import {ImageResize} from 'quill-image-resize-module'  
setTimeout(() => {
  const ImageResize = require("quill-image-resize-module").default

  Quill.register('modules/imageDrop', ImageDrop)
  Quill.register('modules/imageResize', ImageResize)
}, 100);


// window.ir = ImageResize

// Quill.register('modules/imageResize', ImageResize)
// Vue.use(Quill);
Vue.use(VueEditor);