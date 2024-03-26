<template>
  <n-config-provider :theme="darkTheme">
    <n-card class="bac">
      <n-tabs
        class="card-tabs"
        default-value="signin"
        size="large"
        animated
        pane-wrapper-style="margin: 0 -4px"
        pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;"
      >
        <n-tab-pane name="signin" tab="登录">
          <n-form>
            <n-form-item-row label="用户名">
              <input v-model="loginform.loginUsername" placeholder="请输入用户名" />
            </n-form-item-row>
            <n-form-item-row label="密码">
              <input type="password" v-model="loginform.loginPassword" placeholder="请输入密码" />
            </n-form-item-row>
          </n-form>
          <n-button type="primary" block secondary strong @click="login">
            登录
          </n-button>
        </n-tab-pane>
        <n-tab-pane name="signup" tab="注册">
          <n-form>
            <n-form-item-row label="用户名">
              <input v-model="signupform.signupUsername" placeholder="请输入用户名" />
            </n-form-item-row>
            <n-form-item-row label="密码">
              <input type="password" v-model="signupform.signupPassword" placeholder="请输入密码" />
            </n-form-item-row>
            <n-form-item-row label="重复密码">
              <input type="password" v-model="signupform.repeatPassword" placeholder="请再次输入密码" />
            </n-form-item-row>
          </n-form>
          <n-button type="primary" block secondary strong @click="register">
            注册
          </n-button>
        </n-tab-pane>
      </n-tabs>
      <div v-if="isLoggedIn">
        <!-- 显示用户信息或登出按钮 -->
        <p>欢迎，{{ loginform.loginUsername }}</p>
        <n-button type="primary" @click="logout">退出登录</n-button>
      </div>
    </n-card>
  </n-config-provider>
</template>

<script setup lang="ts">
import { darkTheme } from 'naive-ui';
import { reactive, ref } from 'vue';
//路由
import { useRouter} from 'vue-router';
const router = useRouter();
//用户相关小仓库
import useUserStore from '@/store/modules/user';
const userStore = useUserStore();

const loginform=reactive({
  loginUsername: '',
  loginPassword: '',
})
const signupform=reactive({
  signupUsername: '',
  signupPassword: '',
  repeatPassword: '',
})

const isLoggedIn = ref(false);

const login = () => {
  if (loginform.loginUsername === 'test' && loginform.loginPassword === '123456') {
    router.push('/dashboard/person');
  } else {
    alert('登录失败，请检查用户名和密码');
  }
  // userStore.userlogin(loginform);
};

const register = () => {
  if(signupform.signupUsername === '' || signupform.signupPassword === '') {
    alert('用户名和密码不能为空！');
  } else if (signupform.signupPassword !== signupform.repeatPassword) {
    alert('两次输入的密码不一致');
  } else {
    alert('注册成功');
  }
};

const logout = () => {
  isLoggedIn.value = false;
};
</script>

<style scoped>
.card-tabs .n-tabs-nav--bar-type {
  padding-left: 4px;
}
input {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 3px;
  font-size: 14px;
}

input:focus {
  outline: none;
  border-color: #085edf;
  box-shadow: 0 0 5px rgba(0, 116, 235, 0.5);
}


.bac {
  background-color: rgba(21, 20, 20, 0.6);
}
</style>
