SELECT
    ip,
    count(ip) as invalid_count
FROM
    logs
WHERE
    -- leading zero
    ip ~ '[\.^]0'
OR
    -- wrong number of octets
    ip !~ '^[0-9]{1,3}(\.[0-9]{1,3}){3}$'
OR
    -- greater than 255
    ip ~ '25[6-9]|2[6-9][0-9]|[3-9][0-9]{2}'
GROUP BY
    ip
ORDER BY
    invalid_count DESC,
    ip DESC