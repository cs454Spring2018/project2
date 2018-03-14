const fs = require('fs');

const readFile = async name => {
  let contents = await fs.readFileSync(name, 'utf8')
  let [ state, acceptingStates, ...graph ] = contents
    .split('\n').filter(item => item !== '')

  let map = {}
  for (index in graph) {
    let [ state1, state2 ] = graph[index].split('    ') // 3 or 4 not sure from picture
    map[index] = [state1, state2]
  }
  return map
}

const mergeDFA = ([dfa1, dfa2]) => {
  let dfa = {}, track = [], s = new Set()
  if (Object.keys(dfa1).length === 0) return dfa2
  if (Object.keys(dfa2).length === 0) return dfa1

  let [ t1, t2 ] = dfa1[0]
  let [ t3, t4 ] = dfa2[0]

  let nextVal1 = `${t1}${t3}`
  let nextVal2 = `${t2}${t4}`

  track.push(nextVal1, nextVal2)

  while(track.length !== 0) {
    let val = track.shift()
    if (!s.has(val)) {
      s.add(val)
      let [ lhs, rhs ] = val.split('')
      let [ t1, t2 ] = dfa[lhs]
      let [ t3, t4 ] = dfa[rhs]
      dfa[val] = [`${t1}${t3}`, `${t2}${t4}`]
      track.push(`${t1}${t3}`, `${t2}${t4}`)
    }
  }
  return dfa
}

(async () => {
  let data = await Promise.all([readFile('dfa.txt'), readFile('dfa1.txt')])
  let union = mergeDFA(data)
  console.log(union)
})()
