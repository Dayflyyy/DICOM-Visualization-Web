<template>
  <div class="container">
    <div class="slider">
      <div class="logo">
        <logo />
      </div>

      <!-- 滚动组件 -->
      <el-scrollbar class="scrollbar">
        <!-- 菜单 -->
        <el-menu background-color="#001529" text-color="white" router>
          <el-menu-item index="/dashboard/person">个人主页</el-menu-item>
          <el-menu-item index="/dashboard/arrangement">日程安排</el-menu-item>
          <el-menu-item index="/dashboard/analyze">分析影像</el-menu-item>
          <el-menu-item index="/dashboard/manage">病历管理</el-menu-item>
          <el-menu-item index="/dashboard/task">任务列表</el-menu-item>
        </el-menu>
      </el-scrollbar>
    </div>
    <div class="top">
      <div class="top-profile">
        <profilePhoto />
      </div>
    </div>
    <div class="main">
      <!-- 路由出口 -->
      <RouterView v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </RouterView>
    </div>
  </div>
</template>

<script lang="ts" setup>
import logo from "@/layout/logo/index.vue";
import profilePhoto from "@/components/head/profile photo.vue";
//路由
import { useRouter } from "vue-router";
const router = useRouter();
</script>

<style scoped>
.container {
  width: 120%;
  height: 100vh;
  background: rgb(251, 251, 251);
  z-index: 1;
}
.slider {
  width: 260px;
  height: 100vh;
  background-color: #001529;
  z-index: 1;
  .scrollbar {
    width: 100%;
    height: calc(100vh - 50px);
  }
}
.logo {
  padding-top: 10px;
}

.scrollbar {
  margin-top: 40px;
}
.top {
  position: fixed;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 50px;
  left: 260px;
  background: linear-gradient(to right, #adadad, #ffffff);
  z-index: 2;
  .top-profile {
    display: flex;
    align-items: center;
    padding: 0 20px; /* 调整间距 */
  }
}
.main {
  position: absolute;
  padding: 0px;
  left: 260px;
  top: 50px;
  width: calc(100% - 260px);
  height: 92vh;
  overflow: auto;
  background: rgb(250, 250, 250);
  z-index: 1;
}


.fade-enter-from{   /* 进入时的透明度为0 和 刚开始进入时的原始位置通过active透明度渐渐变为1 */  
  opacity: 0;
  transform: translateX(-100%);
}
 
.fade-enter-to{   /*定义进入完成后的位置 和 透明度 */
  transform: translateX(0%);
  opacity: 1; 
}
 
.fade-leave-active,.fade-enter-active {
    transition: all 0.5s ease-out;
}
 
.fade-leave-from { /* 页面离开时一开始的css样式,离开后为leave-to，经过active渐渐透明 */
  transform: translateX(0%);
  opacity: 1;
}
 
.fade-leave-to{   /* 这个是离开后的透明度通过下面的active阶段渐渐变为0 */  
  transform: translateX(100%);
  opacity: 0;
}

</style>
