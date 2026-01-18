#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from collections import namedtuple

# 定义四元式结构
Quad = namedtuple('Quad', ['op', 'arg1', 'arg2', 'res'])

def parse_quad(line):
    s = line.strip()
    if not (s.startswith('(') and s.endswith(')')):
        raise ValueError(f"格式错误，应该是 (op,arg1,arg2,res)：{line}")
    parts = s[1:-1].split(',')
    if len(parts) != 4:
        raise ValueError(f"无法解析四元式（字段数不是4）：{line}")
    return Quad(*(p.strip() for p in parts))

def quad_to_str(q: Quad) -> str:
    return f"({q.op},{q.arg1},{q.arg2},{q.res})"

def constant_propagation(quads):
    consts = {}
    out = []
    for q in quads:
        # 如果是 “assign 常量 -> res”
        if q.op == 'assign' and q.arg1.isdigit() and q.arg2 == '':
            consts[q.res] = q.arg1
            out.append(q)
        else:
            a1 = consts.get(q.arg1, q.arg1)
            a2 = consts.get(q.arg2, q.arg2) if q.arg2 else ''
            out.append(Quad(q.op, a1, a2, q.res))
    return out

def cse(quads):
    exprs = {}
    out = []
    for q in quads:
        if q.op != 'assign':
            key = (q.op, q.arg1, q.arg2)
            if key in exprs:
                out.append(Quad('assign', exprs[key], '', q.res))
            else:
                exprs[key] = q.res
                out.append(q)
        else:
            out.append(q)
    return out

def dead_code_elimination(quads):
    # 找到所有定义的变量和使用的变量
    defs = {q.res for q in quads}
    uses = set()
    for q in quads:
        if q.arg1 and not q.arg1.isdigit():
            uses.add(q.arg1)
        if q.arg2 and not q.arg2.isdigit():
            uses.add(q.arg2)
    # 根变量：那些被定义但未被使用的（程序输出）
    roots = defs - uses
    # 如果没有根，则保留所有常量赋值
    if not roots:
        roots = {q.res for q in quads if q.op == 'assign' and q.arg1.isdigit()}
    used = set(roots)
    keep_rev = []
    # 反向遍历，活性分析
    for q in reversed(quads):
        if q.res in used:
            keep_rev.append(q)
            # 将依赖变量加入活集合
            if q.arg1 and not q.arg1.isdigit():
                used.add(q.arg1)
            if q.arg2 and not q.arg2.isdigit():
                used.add(q.arg2)
    # 恢复原序并保留常量赋值
    keep_set = set(keep_rev)
    out = []
    for q in quads:
        if q in keep_set or (q.op == 'assign' and q.arg1.isdigit() and q.arg2 == ''):
            out.append(q)
    return out

def optimize(quads):
    quads = constant_propagation(quads)
    quads = cse(quads)
    quads = dead_code_elimination(quads)
    return quads

def main(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip()]
    quads = [parse_quad(l) for l in lines]
    opt = optimize(quads)
    with open(out_path, 'w', encoding='utf-8') as f:
        for q in opt:
            f.write(quad_to_str(q) + '\n')
    print(f"优化完成，结果已写入 {out_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("用法: python optimize_ir.py <输入四元式文件> <输出四元式文件>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])