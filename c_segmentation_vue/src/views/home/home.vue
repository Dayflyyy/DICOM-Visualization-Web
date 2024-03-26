<template>
  <div class="container">
    <Head />
    <div class="main-content">
      <div class="left">
        <Show />
      </div>
      <div class="right">
        <Login />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

import Head from '@/components/head/head.vue';
import Show from '@/components/home/show.vue'
import Login from '@/components/home/login-registry.vue'
// import NotLoggedInComponent from '@/components/head/download.vue';
// import LoggedInComponent from '@/components/head/profile photo.vue';



</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* 让容器占据整个视口高度 */
  background-image: url('/src/assets/homebackground/background.jpg'); /* 替换为您的背景图片路径 */
  background-size: cover; /* 背景图片铺满整个容器 */
  background-repeat: no-repeat; /* 禁止背景图片平铺重复 */

}

.main-content {
  display: flex;
  justify-content: space-between;
  margin-top: 120px; /* 向下偏移  */
  flex-grow: 1; /* 让主体内容占据剩余空间 */
}

.left{
  flex-basis: 65%;
  margin-left: 20px;
}
.right {
  flex-basis: 30%; 
  margin-right: 20px; /* 向左移动  */
  margin-top: 40px;
}
</style>