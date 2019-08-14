<template>
  <el-container>
    <div class="empty-message">
      <h1>{{$t('message.welcome_to_vchart')}}</h1>
    </div>
  </el-container>
</template>

<script>
  export default {
    name: "chartEmpty"
  }
</script>

<style scoped>
  .empty-message {
    height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
