<template>
<div id="container">
  <div class="tc-title">
    <el-row :gutter="10" class="tc-title-row">
      <el-col :span="2"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Step</div></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Content</div></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Expected Result</div></div></el-col>
      <el-col :span="6"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Actual Result</div></div></el-col>
      <el-col :span="2"><div class="grid-content bg-purple tc-title-col"><div class="tc-title-inner">Pass</div></div></el-col>
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
          <el-col :span="2"><div class="grid-content bg-purple tc-step-index" v-text="index+1"></div></el-col>
          <el-col :span="6"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.content" placeholder="测试过程"></el-input></el-col>
          <el-col :span="6"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.res1" placeholder="预期输出"></el-input></el-col>
          <el-col :span="6"><el-input type="textarea" class="tc-step-textarea" autosize v-model="step.res2" placeholder="实际输出"></el-input></el-col>
          <el-col :span="2"><el-switch class="tc-step-pass" v-model="step.pass"></el-switch></el-col>
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
  export default {
    data() {
      return {
        dynamic_tc_form: {
          title: '',
          module: '',
          version: '',
          pkg: '',
          author: '',
          date: '',
          steps: [{
            content: '', res1: '', res2: '', pass: true
          }]
        }
      };
    },
    methods: {
      submitForm(form_name) {
        var tc_data= JSON.stringify(this[form_name]);
        console.log(tc_data);
        this.$http.post('http://127.0.0.1:5000/api', tc_data).then(function (response) {
          console.log(response);
        }).catch(function (error) {
          console.log(error);
        });
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
          content: '',
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
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  };
  align: middle;
}
.el-col {
  border-radius: 4px;
}
.tc-title-inner {
  vertical-align: middle;
  display: inline-block;
  height: 44px;
  text-align: center;
  line-height: 44px;
}
.tc_steps {
  height: 44px;
  margin-top: 10px;
}
.tc_submit {
  position: relative;
  margin-bottom: 300px;
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
