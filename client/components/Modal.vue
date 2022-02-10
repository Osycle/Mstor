<template>
  <div>
    <div class="modal">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <div class="cap">
              Добавить
            </div>
            <span class="cap-btn-close">
              <span @click="$emit('modal-manager', 'close')"></span>
            </span>
          </div>
          <div class="modal-content">
            <div class="text-content">
              <textarea name="" id="" v-model="description"></textarea>
            </div>
            <div class="tags-append">
              <tags-input element-id="tags"
                v-model="selectedTags"
                :existing-tags="[
                    { key: 'web-development', value: 'Web Development' },
                    { key: 'php', value: 'PHP' },
                    { key: 'javascript', value: 'JavaScript' },
                ]"
                placeholder="Добавить категорию"
                :typeahead="true"></tags-input>
              </div>
          </div>
          <div class="modal-footer">
            <div class="btn-content">
              <button type="button" class="btn-def" @click="addCell">
                <span>Сохранить</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { TagsInput } from '@seriouslag/vue-tagsinput';
  export default {
    props: ['modal-data', 'modal-manager'],
    data(){
      return {
        selectedTags: null,
        title: "",
        description: "",
        tags: "",
      }
    },    
    computed: {
    },
    components: {
        TagsInput,
    },
    methods: {
      async addCell(){
        const response = await this.$axios.$post("/", {
          action: "insert",
          params: {
            title: this.title,
            description: this.description,
            tags: this.tags,
          }
        })
        if(response.status){
          this.$emit("append", response.cell)
          this.$emit("modal-manager", "close");
        }

        console.log(this.response);
      },
    },
    mounted(){
      console.log(this.modalData)
      console.log("Modal mounted")
    }
  }
</script>

<style lang="scss" scoped>
  .modal{
    position: fixed;
    width: 100%;
    height: 100%;
    background-color: rgba(white, 0.7);
    left: 0;
    top: 0;
    z-index: 100;
  }
  .modal-wrapper{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
  .modal-container{
    width: 600px;
    //border: $border-def;
    padding: 0;

    // filter: 
    //   drop-shadow(2px 2px 0px black) 
    //   drop-shadow(2px -2px 0px black) 
    //   drop-shadow(-2px 2px 0px black) 
    //   drop-shadow(-2px -2px 0px black);
  }
  .modal-header{
    position: relative;
    height: 35px;
    display: flex;
    //background-color: var(--color-1);
    color: white;
    //border: var(--border-def);
  }
  .modal-content{
    //padding: 20px;
    margin: auto;
    .text-content{
      display: flex;
      //border-left: var(--border-def);
      //border-right: var(--border-def);
    }
    textarea{
      width: calc(100% - 40px);
      min-height: 200px;
      //border: 1px solid var(--color-1);
      border: 0;
      resize: none;
      background: var(--color-gray-2);
      padding: 20px 20px;
      &:focus{
        box-shadow: inset 0px 0px 1px 0px var(--color-3);
      }
    }
  }
  .modal-footer{
    height: 45px;
    //background-color: var(--color-1);
    display: flex;
    justify-content: flex-end;
    position: relative;
    //border: var(--border-def);
    .btn-content{
      height: auto;
      align-self: center;
      justify-self: right;
      margin-right: 0;
      .btn-def{
        position: absolute;
        right: -45px;
        bottom: -20px;
        height: 100%;
        background-color: var(--color-3);
        color: var(--color-1);
        padding: 10px 20px;
        font-weight: 600;
        //border-left: var(--border-def);
        &:hover{
          //box-shadow: inset -1px -1px 0px 0px black;
          //animation: var(--animation-sir);
        }
      }
    }
  }
  .tags-append{
    display: none;
  }
  .cap{
    align-self: center;
    padding: 5px 20px;
    background-color: $color-1;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: -17px;
  }
  .cap-btn-close{
    position: absolute;
    right: -65px;
    top: -10px;
    width: 40px;
    height: 100%;
    //border-left: var(--border-def);
    &:hover{
      cursor: pointer;
    }
    span{
      width: 100%;
      height: 100%;
      position: relative;
      display: inline-block;
      background-color: var(--color-3);
      &:hover{
        box-shadow: inset -1px -1px 0px 0px black;
        animation: var(--animation-sir);
      }
      &:before, &:after{
        content: "";
        display: inline-block;
        position: absolute;
        left: calc(50% - 10px);
        top: calc(50% - 1px);
        width: 20px;
        height: 2px;
        background-color: var(--color-1);
      }
      &:before{
        transform: rotate(45deg);
      }
      &:after{
        transform: rotate(-45deg);
      }
    }
  }
  .text-content, .cap, .btn-def, .cap-btn-close{
    //box-shadow: inset 0px 0px 0px 2px black;
    transition: 0.3s ease;
    box-shadow: 
                5px 5px 0px 2px black, 
                -5px -5px 0px 2px black;
    &:hover{
      box-shadow: 
                0px 0px 0px 0px black, 
                -0px -0px 0px 0px black;
    }
  }
</style>

<style lang="scss">
  .tags-input {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
  }

  .tags-input input {
    flex: 1;
    background: transparent;
    border: none;
    &:focus{
      outline: none;
    }
  }

  .tags-input-wrapper-default {
    padding: 15px 20px;
    background-color: $color-gray-1;
    border: 0;
    border-top: 1px solid $color-gray-3;
  }

  .tags-input-wrapper-default.active {
    border-color: $color-3;
  }

  .tags-input span {
    margin-right: .3em
  }

  .tags-input-remove {
    cursor: pointer;
    position: absolute;
    display: inline-block;
    right: .3em;
    top: .3em;
    padding: .5em;
    overflow: hidden
  }

  .tags-input-remove:focus {
    outline: none
  }

  .tags-input-remove:after,.tags-input-remove:before {
    content: "";
    position: absolute;
    width: 75%;
    left: .15em;
    background: #5dc282;
    height: 2px;
    margin-top: -1px
  }

  .tags-input-remove:before {
    transform: rotate(45deg)
  }

  .tags-input-remove:after {
    transform: rotate(-45deg)
  }

  .tags-input-badge {
    position: relative;
    display: inline-block;
    padding: .25em .4em;
    font-size: 75%;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .25em;
    overflow: hidden;
    text-overflow: ellipsis
  }

  .tags-input-badge-pill {
    padding-right: 1.25em;
    padding-left: .6em;
    border-radius: 10em
  }

  .tags-input-badge-pill.disabled {
    padding-right: .6em
  }

  .tags-input-badge-selected-default {
    color: #212529;
    background-color: #f0f1f2
  }

  .typeahead-hide-btn {
    color: #999!important;
    font-style: italic
  }

  .typeahead-badges>span {
    margin-top: .5em;
    cursor: pointer;
    margin-right: .3em
  }

  .typeahead-dropdown {
    list-style-type: none;
    padding: 0;
    margin: 0;
    position: absolute;
    width: 100%;
    z-index: 1000
  }

  .typeahead-dropdown li {
    padding: .25em 1em;
    cursor: pointer
  }

  .tags-input-typeahead-item-default {
    color: #fff;
    background-color: #343a40
  }

  .tags-input-typeahead-item-highlighted-default {
    color: #fff;
    background-color: #007bff!important
  }

</style>