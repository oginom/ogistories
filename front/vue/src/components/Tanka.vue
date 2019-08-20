<template>
<div>
  <div class="tanka-container">
    <div class="tanka-content">{{ message }}</div>
  </div>
  <span class="glyphicon glyphicon-heart"></span>
  <br>ogiogi
  <div>
  <span class="glyphicon glyphicon-heart"></span>
  </div>
  <br>ogiogi
  <div class="flexbox">
  <div class="fav-btn">
    <span href="" class="favme dashicons dashicons-heart"></span>
  </div>
  </div>
  <br>ogiogi
  <br>ogiogi
  <br>ogiogi
  <br>ogiogi
</div>
</template>

<script>
export default {
  data: function () {
    return {
      message: '短歌\nTANKA\nたんか\n2020年'
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
  font-size: 27px;
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

/* https://codepen.io/mapk/pen/ZOQqaQ author: Mapk */
html, body { height:100%; }
.flexbox {
  display: flex;
  height: 100%;
  justify-content: center;
  align-items: center;
}
.fav-btn {
  display:flex;
  height: 100%;
  justify-content: center;
  align-items: center;
}

@keyframes favme-anime {
  0%   {
    opacity: 1;
    font-size: ms(0);
    -webkit-text-stroke-color: transparent;
  }
  25%   {
    opacity:.6;
    color: #FFF;
    font-size: ms(-2);
    -webkit-text-stroke-width: 1px;
     -webkit-text-stroke-color: #DC3232;
  }
  75%   {
    opacity:.6;
    color: #FFF;
    font-size: ms(3);
    -webkit-text-stroke-width: 1px;
     -webkit-text-stroke-color: #DC3232;
  }
  100% {
    opacity: 1;
    font-size: ms(2);
    -webkit-text-stroke-color: transparent;
  }
}

@keyframes favme-hover {
  from {
    font-size: ms(3);
  }
  80% {
    font-size: ms(2);
  }
}

.favme {
  display:block;
  font-size: ms(2);
  width: auto;
  height: auto;
  cursor: pointer;
  box-shadow: none;
  transition: all .2s ease;
  color: #CBCDCE;
  margin: 0;

  &.active {
    color: #DC3232;
  }
  &:hover {
    animation: favme-hover .3s infinite alternate;
  }
  &.is_animating {
    animation: favme-anime .3s;
  }
}
</style>
