<script setup>
import { data as posts } from './posts.data.js'
</script>

<template>
    <ul>
        <li v-for="post of posts">
            <a :href="post.url">{{ post.frontmatter.title }}</a>
        </li>
    </ul>
</template>
