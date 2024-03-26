<template>
  <div class="logo">
    <img src='/src/assets/logo/logo.jpg' alt="" />
    <span class="title">智慧医疗</span>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.logo {
  width: 95%;
  display: flex;
  align-items: center;
  color: #959ea6;
  font-weight: 700;
  flex-wrap: nowrap;
  overflow: hidden;
  padding-left: 50px;
  img {
    display: inline-block;
    widows: 30px;
    height: 30px;
    border-radius: 10px;
  }
  .title {
    display: inline-block;
    height: 32px;
    margin: 2px 0 0 18px;
    overflow: hidden;
    font-size: 18px;
    font-weight: 600;
    line-height: 32px;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
}
</style>
