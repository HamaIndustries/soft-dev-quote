<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { sessionExists, endSession, sess } from './session/sessions';
import SiteHeader from './components/SiteHeader.vue'

function  log_out() {
  endSession()
}
</script>

<template>
  <div class="site">
    <header>
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

      <div class="wrapper">
        <SiteHeader msg="Slick Solutions" />

        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/fuel" v-if="sess.logged_in">Fuel Quote</RouterLink>
          <RouterLink to="/login" v-if="!sess.logged_in">Login</RouterLink>
          <RouterLink to="/register" v-if="!sess.logged_in">Register</RouterLink>
          <RouterLink to="/profileManage" v-if="sess.logged_in">Profile</RouterLink>
          <RouterLink to="/quotehistory" v-if="sess.logged_in">Quote History</RouterLink>
          <RouterLink to="/" v-if="sess.logged_in" @click.native="log_out">Log Out</RouterLink>
        </nav>
      </div>
    </header>

  <RouterView />
  </div>
</template>

<style scoped>
.site {
  display: flex;
  flex-direction: column;
  align-items: center;
}

header {
  line-height: 1.5;
  max-height: 100vh;
  margin-bottom: 3rem;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  font-size: 12px;
  text-align: center;
  margin-top: 2rem; 
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    align-items: center;
    padding-right: calc(var(--section-gap) / 2);
    margin-bottom: 1rem;
    width: 100%;
  }

  .logo {
    margin: 0 1.5rem 1rem 0;
  }

  header .wrapper {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    width: 100%;
    align-items: center;
  }

  nav {
    text-align: right;
    margin-left: auto;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: initial;
  }
}
</style>
