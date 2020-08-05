function solution(n, times) {
  times.sort((a, b) => a - b)

  let left = 1
  let right = times[times.length - 1] * n
  let result = right

  while (left <= right) {
    let mid = Math.floor((left + right) / 2)
    let count = 0

    for (const time of times) {
      count += Math.floor(mid / time)
      if (count >= n) {
        result = Math.min(mid, result)
        break
      }
    }

    if (count >= n) {
      right = mid - 1
    } else {
      left = mid + 1
    }
  }

  return result
}
