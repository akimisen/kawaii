<template>
<div id="container">
  <div class="tc-info">
    <el-row :gutter="10" class="tc-info-row">
      <el-col :span="3"><el-input class="tc-info-inner" v-model="dynamic_tc_form.jira1" placeholder="需求号"></el-input></el-col>
      <el-col :span="6"><el-input class="tc-info-inner" v-model="dynamic_tc_form.pkg" placeholder="专题包"></el-input></el-col>
      <el-col :span="7"><el-input class="tc-info-inner" v-model="dynamic_tc_form.title" placeholder="案例名称"><template slot="prepend">TC</template></el-input></el-col>
      <el-col :span="3"><el-input class="tc-info-inner" v-model="dynamic_tc_form.author" placeholder="作者"></el-input></el-col>
      <el-col :span="3"><el-date-picker type="date" value-format="yyyyMMdd" placeholder="日期" v-model="dynamic_tc_form.date" style="width: 100%;"></el-date-picker></el-col>
      <div class="clearfloat"></div>
    </el-row>
  </div>
  <div class="tc-title">    
    <el-row :gutter="10" class="tc-title-row">
      <el-col :span="1"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Step</div></div></el-col>
      <el-col :span="3"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Prerequisite</div></div></el-col>
      <el-col :span="3"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Testdata</div></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Description</div></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Expected Result</div></div></el-col>
      <el-col :span="4"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Actual Result</div></div></el-col>
      <el-col :span="1"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Pass</div></div></el-col>
    </el-row>
  </div>
  <div class="tc-main">
    <el-form :model="dynamic_tc_form" ref="dynamic_tc_form" label-width="0" class="tc-form">
      <el-form-item
        v-for="(step, index) in dynamic_tc_form.steps"
        class="tc-form-item"
        label=""
      >
        <el-row :gutter="10" class="tc-step-row">
          <el-col :span="1"><div class="grid-content bg-purple tc-step-index" v-text="index+1"></div></el-col>
          <el-col :span="3"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.prerequisite" placeholder="前置条件"></el-input></el-col>
          <el-col :span="3"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.testdata" placeholder="测试数据"></el-input></el-col>
          <el-col :span="6"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.description" placeholder="测试方法"></el-input></el-col>
          <el-col :span="4"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.res1" placeholder="预期输出"></el-input></el-col>
          <el-col :span="4"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.res2" placeholder="实际输出"></el-input></el-col>
          <el-col :span="1"><el-switch class="tc-step-pass" v-model="step.pass"></el-switch></el-col>
          <el-col :span="2"><el-button class="tc-step-button" type="primary" @click.prevent="removeStep(step)">删除</el-button></el-col>
          <div class="clearfloat"></div>
        </el-row>
      </el-form-item>
      <el-form-item class="tc_submit">
        <el-button type="primary" @click="submitForm('dynamic_tc_form')">提交</el-button>
        <el-button @click="addStep">新增</el-button>
        <el-button @click="resetForm('dynamic_tc_form')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</div>
</template>

<script>
  import qs from 'qs';
  export default {
    data() {
      return {
        dynamic_tc_form: {
          api: 'tc_content',
          title: '',
          module: '',
          version: '',
          pkg: '',
          author: '钱秋实',
          date: '',
          steps: [{
            prerequisite: '', testdata: '', description: '', res1: '', res2: '', pass: true
          }]
        }
      };
    },
    methods: {
      submitForm(form_name) {
        var tc_data= JSON.stringify(this[form_name]);
        console.log(tc_data);
        this.$axios.post('http://127.0.0.1:5000/api', tc_data).then(function (response) {
          console.log(response);
        }).catch(function (error) {
          console.log(error);
        });
        // var post = function (url, data, fn) {
        //   var xhr = new XMLHttpRequest();
        //   if (xhr.withCredentials === undefined) return false;
        //   xhr.open("POST", url, true);
        //   xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");  
        //   xhr.onreadystatechange = function() {

        //     if (xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 304)) {
        //       fn.call(this, xhr.responseText);
        //     }
        //   };
        //   xhr.send(data);
        // }
        // var callback = function(res){
        //   console.log(res);
        // }
        // post('http://127.0.0.1:5000/api', tc_data, callback);
      },
      resetForm(form_name) {
        this.$refs[form_name].resetFields();
      },
      removeStep(item) {
        var index = this.dynamic_tc_form.steps.indexOf(item)
        if (index !== -1) {
          this.dynamic_tc_form.steps.splice(index, 1)
        }
      },
      addStep() {
        this.dynamic_tc_form.steps.push({
          prerequisite: '',
          testdata :'',
          description: '',
          res1 : '',
          res2 : '',
          pass : true
        });
      }
    }
  }
</script>

<style>
body {
  overflow: scroll;
  font-size: 14px;
}
.el-form {
  size: small;
}
.el-form-item {
  margin: 0;
}
.el-input {
  size: small;
}
.el-input__inner {
  margin-top: 0;
}
.radiogroup {
  text-align: left;
}
.el-select {
  width: 105px;
}
.el-row {
  margin: 10px 0;
  &:last-child {
    margin-bottom: 0;
  };
  align: middle;
}
.el-col {
  border-radius: 4px;
}
.el-textarea {
  display: inline-block;
  width: 100%;
  vertical-align: middle;
}
.tc-step-index {
  height: 40px;
}
.tc-title-inner {
  vertical-align: middle;
  display: inline-block;
  height: 40px;
  text-align: center;
  line-height: 40px;
}
.tc-info {
  margin: 20px 0;
}
.tc-title {
  margin: 10px 0;
}
.tc-main {
  margin: 10px 0;
}
.clearfloat {
  clear:both;
  height:0;
  font-size: 1px;
  line-height: 0px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
