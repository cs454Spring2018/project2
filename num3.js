const fs = require('fs');

const readFile = async name => {
  let contents = await fs.readFileSync(name, 'utf8')
  let [ state, acceptingStates, ...graph ] = contents
    .split('\n').filter(item => item !== '')

  let map = {}
  for (index in graph) {
    map[index] = graph[index].split('  ')
  }

  return [map, state]
}

const mergeArray = (sArray, bArray) => {
  return bArray.length > sArray.length
    ? bArray.map((elem, i) => elem + '|' + (sArray[i] ? sArray[i] : ''))
    : sArray.map((elem, i) => elem + '|' + (bArray[i] ? bArray[i] : ''))
}


const mergeDFA = data => {
  let mainDFA = {}, s = new Set(), merged;
  let [ [ dfa, states ], [ dfa1, states1 ] ] = data

  if (Object.keys(dfa).length === 0)  return dfa1
  if (Object.keys(dfa1).length === 0) return dfa

  merged = mergeArray(dfa[0], dfa1[0])

  let track = [...merged]
  mainDFA['00'] = merged

  while (track.length !== 0) {
    let val = track.shift();
    if (!s.has(val)) {
      let state1 = val.match(/(\d*)\|/)[1]
      let state2 = val.match(/\|(\d*)/)[1]
      merged = mergeArray(dfa[state1], dfa1[state2]);
      mainDFA[`${state1}${state2}`] = merged;
      track = [...track, ...merged]
      s.add(val);
    }
  }
  return mainDFA
}

const cleanDFA = dfa => {
  let newDFA = {}
  for (item in dfa)
    newDFA[parseInt(item)] = cleanArray(dfa[item])
  return newDFA
}

const cleanArray = array => {
  return array.map(item => {
    let state1 = item.match(/(\d*)\|/)[1]
    let state2 = item.match(/\|(\d*)/)[1]
    return parseInt(`${state1}${state2}`)
  })
}


(async () => {
  let data = await Promise.all([readFile('dfa1.txt'), readFile('dfa2.txt')])
  let union = mergeDFA(data)
  let cleaned = cleanDFA(union)
  console.log(cleaned)
})()
