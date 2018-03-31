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


const mergeDFA = (dfa, dfa1) => {
  let mainDFA = [], newStates = {}, s = new Set(), merged;

  if (Object.keys(dfa).length === 0)  return dfa1
  if (Object.keys(dfa1).length === 0) return dfa

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
      merged = mergeArray(dfa[state1], dfa1[state2]);
      mainDFA.push(merged)
      track = [...track, ...merged]
      s.add(val);
    }
  }
  return [ mainDFA, newStates ]
}


const normalizeDFA = ([mainDFA, newStates]) => {
  //n^2
  for (let i = 0; i < mainDFA.length; i++) {
    fixState(mainDFA[i], newStates)
  }

}


const fixState = (currentTransition, newStates) => {
  let data = ''
  for (let i = 0; i < currentTransition.length; i++) {
    data += `${newStates[currentTransition[i].replace(' ', '')]}\t`
  }
  console.log(data)
}

const createAcceptingStates = (accept, accept1, length) => {
  accept = accept.split(' ')
  accept1 = accept1.split(' ')
  let data = new Set([...accept, ...accept1])
  console.log(data)
  let str = ''
  for (let i = 0; i < length; i++){
    if (isIn(i, data)) {str += `${i} `}
  }
  console.log(str)
}

const isIn = (iValue, data) => {
  iValue = iValue.toString()

  for (let i = 0; i < iValue.length; i++) {
    if (!(data.has(iValue[i]))) {
      return false;
    }
  }
  return true;
}


(async () => {
  let [ [ dfa, states, acceptingStates ], [ dfa1, states1, acceptingStates1 ] ] =
      await Promise.all([readFile('dfa1.txt'), readFile('dfa2.txt')])
  let union = mergeDFA(dfa, dfa1)
  console.log(union)
  createAcceptingStates(acceptingStates, acceptingStates1, union[0].length)
  normalizeDFA(union)



})()
