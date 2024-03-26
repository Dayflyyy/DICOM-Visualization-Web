<template>
    <n-carousel
      effect="card"
      prev-slide-style="transform: translateX(-150%) translateZ(-800px);"
      next-slide-style="transform: translateX(50%) translateZ(-800px);"
      style="height: 400px"
      :show-dots="false"
    >
      <n-carousel-item :style="{ width: '60%' }">
        <img
          class="carousel-img"
          src="/src/assets/homeshow/show1.jpg"
        >
      </n-carousel-item>
      <n-carousel-item :style="{ width: '60%' }">
        <img
          class="carousel-img"
          src="/src/assets/homeshow/show2.jpg"
        >
      </n-carousel-item>
      <n-carousel-item :style="{ width: '60%' }">
        <img
          class="carousel-img"
          src="/src/assets/homeshow/show3.jpg"
        >
      </n-carousel-item>
      <n-carousel-item :style="{ width: '60%' }">
        <img
          class="carousel-img"
          src="/src/assets/homeshow/show4.jpg" 
        >
      </n-carousel-item>
    </n-carousel>
  </template>
  
  <style scoped>
  .carousel-img {
    margin: 0 auto;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  </style>