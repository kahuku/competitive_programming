/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    function rearrange(word) {
        const s_arr = word.split("");
        const sorted = s_arr.sort();
        const joined = sorted.join('');
        return joined;
    }
    let map = new Map();
    for (const str of strs) {
        const normalized = rearrange(str);
        if (!map.has(normalized)) {
            map.set(normalized, []);
        }
        const previous_group = map.get(normalized);
        const group = [...previous_group, str];
        map.set(normalized, group);
    }
    let list = [];
    for (const [key, value] of map.entries()) {
        list.push(value);
    }
    return list;
};

var groupAnagrams = function(strs) {
    const map = new Map();
    for (const str of strs) {
        const key = [...str].sort().join('');
        if (!map.has(key)) map.set(key, []);
        map.get(key).push(str);
    }
    return [...map.values()];
};