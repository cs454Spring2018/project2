const fs = require('fs');

const readFile = async name => {
  let contents = await fs.readFileSync(name, 'utf8')
  let [ state, acceptingStates, ...graph ] = contents
    .split('\n').filter(item => item !== '')

  let map = {}
  for (index in graph) {
    map[index] = graph[index].split('  ')
  }
  return [map, state, acceptingStates]
}

const mergeArray = (sArray, bArray) => {
  return bArray.length > sArray.length
    ? bArray.map((elem, i) => elem + '|' + (sArray[i] ? sArray[i] : ''))
    : sArray.map((elem, i) => elem + '|' + (bArray[i] ? bArray[i] : ''))
}


const mergeDFA = (dfa, dfa1, accept, accept1) => {
  let mainDFA = [], newStates = {}, s = new Set(), merged, accepting = [];

  if (Object.keys(dfa).length === 0)  return dfa1
  if (Object.keys(dfa1).length === 0) return dfa

  accept = new Set(accept)
  accept1 = new Set(accept1)

  merged = mergeArray(dfa[0], dfa1[0])
  let track = [...merged]
  mainDFA.push(merged)
  newStates['0|0'] = 0;
  s.add('0|0')
  let stateTrack = 1;


  while (track.length !== 0) {
    let val = track.shift();
    val = val.replace(' ', '')
    if (!s.has(val)) {
      newStates[val] = stateTrack++;
      let state1 = val.match(/(\d*)\|/)[1]
      let state2 = val.match(/\|(\d*)/)[1]

      if (accept.has(state1) && accept1.has(state2)) { accepting.push(val); }
      merged = mergeArray(dfa[state1], dfa1[state2]);
      mainDFA.push(merged)
      track = [...track, ...merged]
      s.add(val);
    }
  }
  return [ mainDFA, newStates, accepting ]
}


const normalizeDFA = ([mainDFA, newStates]) => {
  for (let i = 0; i < mainDFA.length; i++) {
    fixState(mainDFA[i], newStates)
  }
}

const fixState = (currentTransition, newStates) => {
  let data = ''
  for (let i = 0; i < currentTransition.length; i++)
    data += `${newStates[currentTransition[i].replace(' ', '')]}\t`
  console.log(data)
}

const printAcceptingStates = (newStates, accepting) => {
  let str = ''
  for (let i = 0; i < accepting.length; i++)
    str += `${newStates[accepting[i]]}  `
  console.log(str)
}


(async () => {
  let [ [ dfa, states, acceptingStates ], [ dfa1, states1, acceptingStates1 ] ] =
      await Promise.all([readFile('dfa1.txt'), readFile('dfa2.txt')])
  let [ mainDFA, newStates, accepting ] = mergeDFA(dfa, dfa1, acceptingStates, acceptingStates1)
  console.log(Object.keys(newStates).length)
  printAcceptingStates(newStates, accepting)
  normalizeDFA([mainDFA, newStates])
})()
