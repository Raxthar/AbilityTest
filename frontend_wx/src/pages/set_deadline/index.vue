<template>
   <div>
      <i-radio :value="是否设置自动评价" :disabled="disabled" :checked="checked" @change="handleAnimalChange">
      </i-radio>
      <i-radio :value="是否设置截止日期" :disabled="disabled2" :checked="checked2" @change="handleAnimalChange2">
      </i-radio>
     <i-input v-model="deadline_date" type="textarea"  placeholder="请输入详细地址(最多50字)" maxlength="50" />
 </div>

</template>

<script>

  export default {

    data () {
      return {
        deadline_date:"",
        animal: '熊猫',
        checked: false,
        disabled: false,
        checked2: false,
        disabled2: false
      }

    },

    methods: {
      handleAnimalChange ({mp}) {
       this.checked = mp.detail.current
      },
      handleAnimalChange2 ({mp}) {
       this.checked = mp.detail.current
      }
    }
  }

</script>



<style lang="less">

</style>