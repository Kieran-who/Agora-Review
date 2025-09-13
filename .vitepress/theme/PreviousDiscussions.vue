<script setup>
import { data as posts } from './posts.data.js'
</script>

<template>
    <ul>
        <li v-for="post of posts">
            <a :href="post.url">{{ post.frontmatter.title.replace('_', ":") }}</a>
        </li>
    </ul>
</template>
