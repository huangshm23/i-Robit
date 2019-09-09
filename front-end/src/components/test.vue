<template>
    <el-menu :default-active="activeIndex" mode="horizontal" background-color="#284EA5" text-color="#fff" active-text-color="#ffd04b">
        <el-menu-item index="1">
            <router-link :to="{ path: '/recommendation' }">组合推荐</router-link>
        </el-menu-item>
        <el-menu-item index="2">
            <router-link :to="{ path: '/news' }">新闻推荐</router-link>
        </el-menu-item>
        <el-menu-item index="3">
            <router-link :to="{ path: '/'}" @click.native="tuichu">退出账号</router-link>
        </el-menu-item>
    </el-menu>
    
</template>

<script>
    export default {
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1'
            };
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },
            tuichu(){
                this.$store.state.is_login=false;
                this.$router.push('/signin')
            }
        }
    }
</script>