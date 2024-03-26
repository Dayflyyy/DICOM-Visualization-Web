<template>
  <div class="top-bar">
    <div class="logo-container">
      <img src="/src/assets/logo/logo.jpg" alt="logo" class="logo">
    </div>
    <h1 class="text">智慧医疗</h1>
    <div class="menu-container">
      <!-- <profilePhoto/> -->
    </div>
  </div>
</template>

<script lang="ts" setup>
  import profilePhoto from './profile photo.vue';
</script>

<style scoped>
.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: black; /* 背景黑色 */
  color: white; /* 文字颜色为白色 */
  padding: 10px 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  display: flex;
  justify-content: space-between; /* 两个元素在一行显示，space-between使它们平均分布 */
  align-items: center; /* 垂直居中对齐 */
}

.logo-container {
  background-color: #fff; /* 图片容器背景色为白色 */
  padding: 5px; /* 添加内边距 */
  border-radius: 50%; /* 圆形边框 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.logo {
  width: 50px;
  height: 50px; /* 设置图片大小 */
  border-radius: 50%; /* 圆形边框 */
}

.text {
  margin: 0; /* 去除默认的外边距 */
  line-height: 1; /* 垂直居中 */
  padding-left: 50px; /* 左边距为10px（根据需求调整） */
}

.menu-container {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* 将menu-container内容靠右对齐 */
  gap: 10px; /* 菜单项之间的间距 */
  padding-right: 30px;
}
</style>
