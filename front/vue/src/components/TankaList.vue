<template>
<div>
  <div class="tanka-container">
    <center>おすすめ</center>
    <router-link to="/tanka/1">
      <div class="tanka-content">{{ recommend_message }}</div>
    </router-link>
  </div>
  <div class="tanka-container">
    <center>新着</center>
    <router-link to="/tanka/1">
      <div class="tanka-content">{{ new_message }}</div>
    </router-link>
  </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {
      recommend_message: '風吹けば…',
      new_message: '春過ぎて…'
    }
  }
}
</script>

<style scoped>
.tanka-content {
  display: inline-block;
  background: #CCCCFF;
  font-family: 'Yu Mincho', YuMincho, 'Hiragino Mincho ProN', 'Hiragino Mincho Pro', 'HGP明朝B', serif;
  -webkit-font-feature-settings: 'pkna';
          font-feature-settings: 'pkna';
  font-size: 17px;
  line-height: 1.9;
  letter-spacing: 0.03em;
  -webkit-writing-mode: vertical-rl;
      -ms-writing-mode: tb-rl;
          writing-mode: vertical-rl;

  text-orientation: upright; /* alphabetも縦 */
  /* text-align: center;
  vertical-align: center; */
  /* position: absolute;
  right: 0; */
}

.tanka-container {
  margin-top: 60px;
}
</style>
